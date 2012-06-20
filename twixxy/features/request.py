def request(self, req):
    return self.fields(method=req.method, uri=req.uri)
