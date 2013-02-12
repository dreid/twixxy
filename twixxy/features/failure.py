def failure(self, f):
    return self.trace((f.type, f.value, f.tb))
