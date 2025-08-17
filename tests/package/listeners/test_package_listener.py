from tkc_api_rest.package.events import PackageEvent

def test_package_listener():
    PackageEvent.Dispatch(event_type="created", id=1)
    assert 1 == 1