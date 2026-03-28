import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://ramdesh.github.io"
DIRECTORIES = ["english-stories", "sinhala-stories"]

def get_local_html_files(directory):
    files = []
    dir_path = os.path.join(os.path.dirname(__file__), "..", directory)
    for f in os.listdir(dir_path):
        if f.endswith(".html"):
            files.append(f)
    return files

def get_title_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.title.string.strip() if soup.title else None

def test_sync():
    print("Starting regression tests for live site synchronization...")
    all_passed = True

    # Also test the root index.html
    files_to_test = {
        "": ["index.html"]
    }
    for d in DIRECTORIES:
        files_to_test[d] = get_local_html_files(d)

    for directory, files in files_to_test.items():
        for filename in files:
            local_path = os.path.join(os.path.dirname(__file__), "..", directory, filename)
            live_url = f"{BASE_URL}/{directory}/{filename}" if directory else f"{BASE_URL}/{filename}"
            
            print(f"Testing {live_url}...")
            
            # Read local file
            with open(local_path, 'r', encoding='utf-8') as f:
                local_content = f.read()
            local_title = get_title_from_html(local_content)

            # Fetch live file
            try:
                response = requests.get(live_url)
                response.raise_for_status()
                live_content = response.text
                live_title = get_title_from_html(live_content)

                if local_title == live_title:
                    print(f"  [PASS] Titles match: '{local_title}'")
                else:
                    print(f"  [FAIL] Title mismatch!")
                    print(f"    Local: '{local_title}'")
                    print(f"    Live:  '{live_title}'")
                    all_passed = False
            except Exception as e:
                print(f"  [ERROR] Could not fetch live URL: {e}")
                all_passed = False

    if all_passed:
        print("\nAll regression tests passed! Local and live sites are in sync.")
    else:
        print("\nSome regression tests failed. Please investigate.")
        exit(1)

if __name__ == "__main__":
    test_sync()
