class Position:
    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= 90):
            raise ValueError(f"Incorrect {latitude} latitude")
        if not (-180 <= longitude <= 180):
            raise ValueError(f"Incorrect {longitude} longitude")
        
        self._latitude = latitude
        self._longitude = longitude


    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude


    def __repr__(self) -> str:
        return f"{self.typename()}(latitude={self.latitude}, longitude={self.longitude})"

    def typename(self):
        return type(self).__name__ 

class EarthPosition(Position):
    pass

class MarsPosition(Position):
    pass
    
if __name__ == '__main__':
    p = Position(29.979, 31.134)
    e = EarthPosition(29.979, 31.134)
    m = MarsPosition(29.979, 31.134)
    print(p)
    print(e)
    print(m)
    # print(p.__repr__())
