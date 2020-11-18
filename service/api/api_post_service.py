

def api_post_service(data):
    val1 = data.get("val1")
    val2 = data.get("val2")
    val3 = data.get("val3")
    val4 = data.get("val4")

    print(val1,val2,val3,val4)

    return True, "ok", 1