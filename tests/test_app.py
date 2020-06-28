
def test_app_is_created(app):
    assert app.name == "chico_delivery.app"

def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_returns_404(client):
    assert client.get("/url_que_não existe").status_code == 404
