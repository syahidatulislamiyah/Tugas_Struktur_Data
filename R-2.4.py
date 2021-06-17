class Flower:
    def __init__(self, nama, jml_kelopak, harga):
        self.nama = nama
        self.jml_kelopak = jml_kelopak
        self.harga = harga

    def set_nama(self,new_nama):
        self.nama=new_nama

    def set_jml_kelopak(self,new_jml_kelopak):
        self.nama=new_jml_kelopak

    def harga(self,new_harga):
        self.nama=new_harga

flower1 = Flower("Mawar",7,12000)
print("Bunga ", flower1.nama,"banyak kelopak ", flower1.jml_kelopak,"seharga ", flower1.harga)

