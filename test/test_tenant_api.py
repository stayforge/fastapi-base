from dotenv import load_dotenv
from starlette.testclient import TestClient

from main import app

load_dotenv()
client = TestClient(app)

AUTH = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtMjZlaTFlZzUybnd3bDZsMi51cy5hdXRoMC5jb20vIn0..Zjj4n8M0FFJLfB6v.UZ3P67B58MBD_PpErm3fGBdDL3QkjkTrC1UCf6jn8lTIuZ-EpudrQknkb9WVIvZth6189Virb6i1tb9bYHnO7rOvWSPBcj_SY_Pxes8dronLRDGvv-UvT4170LMi3teO3nROVeSGbSEvt5cPA-aw8LTVygCcIbJ_JiR-Kp3k7vMwNe312TlN45diXjerHlTtoAFk8H2y3T4xKTeEl9vf8P2YJ9oyPFKY5tOiZoHsw3MhEtIXjfDo_OLLWdLQHIQVqKhlOVpcJWQFii82FAuivGy90gTrTrI4V7ViqpEicZ-Sh5dvymFPJGxS1g1Cj1NJUfqNEx8Rrj4xSRLvEv9e693LgzRSNLWfb5aXdcOLW2BHcGxyyQ4.8K1hLmP-Fna_2DsncdskfQ"
headers_ok = {"Authorization": f"Bearer {AUTH}"} if AUTH else {}


def test_create_tenant(test_db):
    payload = {
        "name": "My tenant",
        "description": "string",
        "environment": "development",
        "stripe_customer_id": "string",
        "metadata": {}
    }

    response = client.post("/tenant/create", json=payload, headers=headers_ok)
    print(response.json())
    assert response.status_code == 200