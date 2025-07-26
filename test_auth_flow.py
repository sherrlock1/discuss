#!/usr/bin/env python3
"""
Test script to verify the complete authentication flow
"""
import requests
import json

BASE_URL = "https://work-1-otvuwyhcdtyibpym.prod-runtime.all-hands.dev"

def test_login_flow():
    print("🔍 Testing Complete Authentication Flow")
    print("=" * 50)
    
    # Step 1: Test login
    print("1. Testing login...")
    login_data = {
        "email": "test@example.com",
        "password": "testpass123"
    }
    
    response = requests.post(f"{BASE_URL}/rest-auth/login/", json=login_data)
    print(f"   Login Status: {response.status_code}")
    
    if response.status_code == 200:
        login_result = response.json()
        token = login_result.get('key')
        print(f"   ✅ Login successful! Token: {token[:20]}...")
        
        # Step 2: Test authenticated user endpoint
        print("\n2. Testing authenticated user endpoint...")
        headers = {"Authorization": f"Token {token}"}
        
        auth_response = requests.get(f"{BASE_URL}/api/v1/users/auth/", headers=headers)
        print(f"   Auth Status: {auth_response.status_code}")
        
        if auth_response.status_code == 200:
            user_data = auth_response.json()
            print(f"   ✅ User data retrieved successfully!")
            print(f"   Username: {user_data.get('username')}")
            print(f"   Email: {user_data.get('email')}")
            print(f"   User ID: {user_data.get('id')}")
            
            # Step 3: Test is_authenticated endpoint
            print("\n3. Testing is_authenticated endpoint...")
            is_auth_response = requests.get(f"{BASE_URL}/api/v1/is_authenticated/", headers=headers)
            print(f"   Is Auth Status: {is_auth_response.status_code}")
            
            if is_auth_response.status_code == 200:
                auth_status = is_auth_response.json()
                print(f"   ✅ Authentication status: {auth_status}")
            else:
                print(f"   ❌ Authentication check failed: {is_auth_response.text}")
                
        else:
            print(f"   ❌ Failed to get user data: {auth_response.text}")
            
    else:
        print(f"   ❌ Login failed: {response.text}")
    
    # Step 4: Test image loading
    print("\n4. Testing image loading...")
    image_urls = [
        f"{BASE_URL}/static/assets/favicon/apple-touch-icon.png",
        f"{BASE_URL}/static/assets/images/default_user.png"
    ]
    
    for url in image_urls:
        img_response = requests.get(url)
        print(f"   {url.split('/')[-1]}: {img_response.status_code} ({len(img_response.content)} bytes)")
    
    print("\n" + "=" * 50)
    print("🎯 Authentication Flow Test Complete!")

if __name__ == "__main__":
    test_login_flow()
