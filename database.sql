-- Active: 1745938775538@@127.0.0.1@5432@bila_cuci_montor@public
CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL,
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE admins (
    id_admin SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    nomor_hp VARCHAR(20),
    status BOOLEAN NOT NULL DEFAULT true,
    id_user INT REFERENCES users(id_user) NOT NULL
);

CREATE TABLE karyawan (
    id_karyawan SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    nomor_hp VARCHAR(20),
    alamat TEXT,
    role VARCHAR(20) NOT NULL,
    tanggal_masuk DATE NOT NULL DEFAULT now(),
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE members (
    id_member SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    nomor_hp VARCHAR(20),
    alamat TEXT,
    tanggal_daftar DATE NOT NULL DEFAULT now(),
    tanggal_berakhir DATE,
    status BOOLEAN NOT NULL DEFAULT false,
    id_user INT REFERENCES users(id_user) NOT NULL
);

CREATE TABLE paket_member (
    id_paket SERIAL PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    harga INT NOT NULL,
    durasi INT NOT NULL, 
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE pembayaran_member (
    id_pembayaran SERIAL PRIMARY KEY,
    id_member INT REFERENCES members(id_member) NOT NULL,
    id_paket INT REFERENCES paket_member(id_paket) NOT NULL,
    tanggal TIMESTAMP NOT NULL DEFAULT NOW(),
    total INT NOT NULL
);

CREATE TABLE metode_pembayaran (
    id_metode SERIAL PRIMARY KEY,
    nama_metode VARCHAR(50) NOT NULL,
    status BOOLEAN NOT NULL
);

CREATE TABLE transaksi (
    id_transaksi SERIAL PRIMARY KEY,
    id_member INT REFERENCES members(id_member),
    id_karyawan INT REFERENCES karyawan(id_karyawan) NOT NULL,
    id_metode INT REFERENCES metode_pembayaran(id_metode),
    tanggal DATE NOT NULL DEFAULT NOW(),
    uang INT,
    total INT
);

CREATE TABLE layanan (
    id_layanan SERIAL PRIMARY KEY,
    nama_layanan VARCHAR(50) NOT NULL,
    harga INT NOT NULL,
    status BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE detail_transaksi (
    id_detail SERIAL PRIMARY KEY,
    id_transaksi INT REFERENCES transaksi(id_transaksi) NOT NULL,
    id_layanan INT REFERENCES layanan(id_layanan) NOT NULL,
    plat VARCHAR(15) NOT NULL,
    nama_kendaraan VARCHAR(50) NOT NULL,
    subtotal INT
);

ALTER TABLE "detail_transaksi" ALTER COLUMN "tanggal" SET DEFAULT now() ;

select sum(transaksi.total)
from transaksi

SELECT SUM(transaksi.total) FROM transaksi

SELECT tanggal, sum(total) FROM transaksi WHERE total > 0 GROUP BY tanggal, total

SELECT DATE(tanggal), sum(total) FROM pembayaran_member GROUP BY DATE(tanggal), total ORDER BY DATE(tanggal) DESC

SELECT m.tanggal_daftar,u.username, m.nama, COALESCE(TO_CHAR(m.tanggal_berakhir, 'YYYY-MM-DD'), 'non aktif') as tanggal_berakhir  FROM users u JOIN members m ON u.id_user = m.id_user ORDER BY m.tanggal_daftar DESC

SELECT to_char(dt.tanggal, 'yyyy-mm-dd, hh:mi:ss'), k.nama, m.nama, dt.subtotal, mp.nama_metode,dt.nama_kendaraan, dt.plat FROM transaksi t FUll JOIN detail_transaksi dt on t.id_transaksi = dt.id_transaksi FUll JOIN karyawan k ON t.id_karyawan = k.id_karyawan FULL JOIN metode_pembayaran mp ON mp.id_metode = t.id_metode LEFT JOIN members m ON t.id_member = m.id_member ORDER BY dt.tanggal DESC