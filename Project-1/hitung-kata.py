def hitung_kata(teks):
    kata = teks.split()
    jumlah_kata = len(kata)
    return jumlah_kata

teks_pengguna = input("Masukkan kalimat atau paragraf: ")
jumlah = hitung_kata(teks_pengguna)

print(f"Jumlah kata dalam teks: {jumlah}")