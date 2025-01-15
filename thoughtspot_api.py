import requests

def get_thoughtspot_token():
    url = 'https://evernorth-dev.thoughtspot.cloud/api/rest/2.0/auth/session/token'
    
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer QzhENlBEOkpITm9hWEp2TVNSVFNFRXRNalUySkRVd01EQXdNQ1JxYW1SRlZ6aHJRemhMWkhkNVdXWjJNa1l5TTBoblBUMGtSRGhsVTNsT1NHMVhTa2RsWVhVMVIwRlpha3d2UkRScFNtbFNNWEpaZUdWUWVXeENZalpHV21SRlNUMA=='
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

if __name__ == "__main__":
    result = get_thoughtspot_token()
    if result:
        print("API Response:")
        print(result)
