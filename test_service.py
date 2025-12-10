"""
Simple test script to verify the service is working
Run this AFTER starting the service with: uvicorn app:app --reload
"""
import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def test_health_check():
    """Test the health endpoint"""
    print("🔍 Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print(f"✅ Health check passed: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: Status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to service. Is it running?")
        print("   Start it with: uvicorn app:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_generate_endpoint():
    """Test the text generation endpoint"""
    print("\n🔍 Testing generate endpoint...")
    try:
        prompt = "Hello, how are you?"
        print(f"   Sending prompt: '{prompt}'")
        
        response = requests.post(
            f"{BASE_URL}/generate",
            params={"prompt": prompt}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Generate endpoint works!")
            print(f"   Generated text: {data['generated_text'][:100]}...")
            print(f"   Latency: {data['latency_seconds']:.4f}s")
            return True
        else:
            print(f"❌ Generate endpoint failed: Status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 50)
    print("🧪 Testing LLM Inference Service")
    print("=" * 50)
    
    # Test health check
    health_ok = test_health_check()
    
    if not health_ok:
        print("\n⚠️  Service is not running. Please start it first:")
        print("   uvicorn app:app --reload")
        return
    
    # Test generate endpoint
    generate_ok = test_generate_endpoint()
    
    print("\n" + "=" * 50)
    if health_ok and generate_ok:
        print("✅ All tests passed! Service is working correctly.")
    else:
        print("❌ Some tests failed. Check the errors above.")
    print("=" * 50)

if __name__ == "__main__":
    main()

