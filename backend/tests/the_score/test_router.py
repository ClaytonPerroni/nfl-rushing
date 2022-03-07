
def test_search_name(client):
    response = client.get("/rushing-stats/?query=jay cutler")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert response.get('results')[0].get('player') == "Jay Cutler"

def test_ordered_by_yards(client):
    response = client.get("/rushing-stats/")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert response.get('results')[0].get('yds') >  response.get('results')[1].get('yds')

def test_ordered_by_yards_asc(client):
    response = client.get("/rushing-stats/?order_direction=asc")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert response.get('results')[0].get('yds') <=  response.get('results')[1].get('yds')

def test_ordered_by_lng(client):
    response = client.get("/rushing-stats/?order_by=lng")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert int(response.get('results')[0].get('lng').replace('T','')) >=  int(response.get('results')[1].get('lng').replace('T',''))

def test_ordered_by_lng_asc(client):
    response = client.get("/rushing-stats/?order_direction=asc&order_by=lng")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert int(response.get('results')[0].get('lng').replace('T','')) <=  int(response.get('results')[1].get('lng').replace('T',''))

def test_ordered_by_lng(client):
    response = client.get("/rushing-stats/?order_by=td")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert response.get('results')[0].get('td')>=  response.get('results')[1].get('td')
def test_ordered_by_td_asc(client):
    response = client.get("/rushing-stats/?order_direction=asc&order_by=td")
    assert response.status_code == 200
    response = response.json()
    print(response)
    assert response.get('results')[0].get('td') <=  response.get('results')[1].get('td')