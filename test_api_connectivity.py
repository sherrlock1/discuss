#!/usr/bin/env python3
"""
Test script to verify API connectivity and CORS settings
"""
import requests
import json

def test_api_endpoint():
    """Test the Django API endpoint that Angular is trying to access"""
    
    # Test the API endpoint directly
    api_url = "https://work-1-otvuwyhcdtyibpym.prod-runtime.all-hands.dev/api/v1/users/auth/"
    
    print("Testing Django API endpoint...")
    print(f"URL: {api_url}")
    
    # Test without CORS headers
    try:
        response = requests.get(api_url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        print(f"Headers: {dict(response.headers)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test with CORS headers (simulating Angular request)
    headers = {
        'Origin': 'https://work-2-otvuwyhcdtyibpym.prod-runtime.all-hands.dev',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    print("Testing with CORS headers (simulating Angular request)...")
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        print(f"CORS Headers in Response:")
        for header, value in response.headers.items():
            if 'cors' in header.lower() or 'access-control' in header.lower():
                print(f"  {header}: {value}")
    except Exception as e:
        print(f"Error: {e}")

def test_angular_app():
    """Test if the Angular app is loading"""
    
    app_url = "https://work-2-otvuwyhcdtyibpym.prod-runtime.all-hands.dev/django_reddit"
    
    print("Testing Angular app loading...")
    print(f"URL: {app_url}")
    
    try:
        response = requests.get(app_url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {len(response.text)} bytes")
        
        # Check if main Angular files are referenced
        if 'main.js' in response.text:
            print("✅ main.js is referenced in HTML")
        else:
            print("❌ main.js is NOT referenced in HTML")
            
        if 'styles.js' in response.text:
            print("✅ styles.js is referenced in HTML")
        else:
            print("❌ styles.js is NOT referenced in HTML")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api_endpoint()
    print("\n" + "="*50 + "\n")
    test_angular_app()