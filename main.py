import requests
import json
import base64
from pathlib import Path

API_URL = "http://127.0.0.1:5001/v1alpha/convert/source"
INPUTS_DIR = Path("inputs")
OUTPUTS_DIR = Path("outputs")

def setup_directories():
    """Create output directory if it doesn't exist."""
    OUTPUTS_DIR.mkdir(exist_ok=True)

def validate_inputs_directory():
    """Check if inputs directory exists."""
    if not INPUTS_DIR.exists():
        print("inputs directory not found")
        return False
    return True

def prepare_request_options():
    """Prepare common request options."""
    return {
        "to_formats": ["json"],
        "table_mode": "accurate",
        "ocr_lang": ["ja", "en"]
    }

def encode_file_to_base64(file_path: Path):
    """Encode file content to base64 string."""
    with open(file_path, 'rb') as f:
        file_content = f.read()
        base64_content = base64.b64encode(file_content).decode('utf-8')
        return base64_content

def convert_file(file_path: Path):
    """Convert a single file and save the result."""
    print(f"Processing: {file_path.name}")
    
    # ファイルをbase64エンコード
    base64_content = encode_file_to_base64(file_path)
    
    # リクエストデータを準備
    request_data = {
        "options": prepare_request_options(),
        "file_sources": [{
            "base64_string": base64_content,
            "filename": file_path.name
        }]
    }
    
    # JSON形式でPOST送信
    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
    
    response = requests.post(API_URL, json=request_data, headers=headers)
    response.raise_for_status()
    
    save_result(file_path, response.json())

def save_result(file_path: Path, result: dict):
    """Save conversion result to output file."""
    output_filename = file_path.stem + ".json"
    output_path = OUTPUTS_DIR / output_filename
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(result, output_file, ensure_ascii=False, indent=2)
    
    print(f"Saved: {output_path}")

def process_file_with_error_handling(file_path: Path):
    """Process a file with error handling."""
    try:
        convert_file(file_path)
    except requests.exceptions.RequestException as e:
        print(f"Request error for {file_path.name}: {e}")
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

def convert_documents():
    """Convert all documents in the inputs directory."""
    setup_directories()
    
    if not validate_inputs_directory():
        return
    
    for file_path in INPUTS_DIR.iterdir():
        if file_path.is_file():
            process_file_with_error_handling(file_path)

if __name__ == "__main__":
    convert_documents()