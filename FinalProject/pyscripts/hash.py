import hashlib


def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

print(hash_data('&xHYEDPrv5'))
print('e4a15bb1f47b2d3ceb49984dfae7d2916cf0e964953ac60680e252c162ee0e32')
