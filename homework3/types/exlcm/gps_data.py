"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class gps_data(object):
    __slots__ = ["timestamp", "latitude", "lat_bearing", "longitude", "long_bearing", "altitude"]

    def __init__(self):
        self.timestamp = 0
        self.latitude = 0.0
        self.lat_bearing = ""
        self.longitude = 0.0
        self.long_bearing = ""
        self.altitude = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(gps_data._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qd", self.timestamp, self.latitude))
        __lat_bearing_encoded = self.lat_bearing.encode('utf-8')
        buf.write(struct.pack('>I', len(__lat_bearing_encoded)+1))
        buf.write(__lat_bearing_encoded)
        buf.write(b"\0")
        buf.write(struct.pack(">d", self.longitude))
        __long_bearing_encoded = self.long_bearing.encode('utf-8')
        buf.write(struct.pack('>I', len(__long_bearing_encoded)+1))
        buf.write(__long_bearing_encoded)
        buf.write(b"\0")
        buf.write(struct.pack(">d", self.altitude))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != gps_data._get_packed_fingerprint():
            raise ValueError("Decode error")
        return gps_data._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = gps_data()
        self.timestamp, self.latitude = struct.unpack(">qd", buf.read(16))
        __lat_bearing_len = struct.unpack('>I', buf.read(4))[0]
        self.lat_bearing = buf.read(__lat_bearing_len)[:-1].decode('utf-8', 'replace')
        self.longitude = struct.unpack(">d", buf.read(8))[0]
        __long_bearing_len = struct.unpack('>I', buf.read(4))[0]
        self.long_bearing = buf.read(__long_bearing_len)[:-1].decode('utf-8', 'replace')
        self.altitude = struct.unpack(">d", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if gps_data in parents: return 0
        tmphash = (0x848027e0673b975d) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if gps_data._packed_fingerprint is None:
            gps_data._packed_fingerprint = struct.pack(">Q", gps_data._get_hash_recursive([]))
        return gps_data._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
