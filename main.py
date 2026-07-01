#!/usr/bin/env python3

import os

def clear():
    os.system("clear")

def banner():
    clear()
    print("╔══════════════════════════════╗")
    print("║      ROBLOX REJOIN V2        ║")
    print("╚══════════════════════════════╝")
    print("RIFT") 
 

while True:
    banner()

    print("[1] Mulai Monitor")
    print("[2] Pilih Package")
    print("[3] Ubah Link")
    print("[4] Pengaturan")
    print("[5] Lihat Log")
    print("[6] Keluar")
    print()

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        clear()
        print("=== MULAI MONITOR ===")
        input("\nTekan ENTER untuk kembali...")

    elif pilih == "2":
    clear()
    print("=== PILIH PACKAGE ===\n")

    result = os.popen("pm list packages | grep roblox").read().splitlines()

    if not result:
        print("Tidak ada package Roblox ditemukan.")
        input("\nTekan ENTER...")
        continue

    packages = []

    for i, p in enumerate(result, 1):
        p = p.replace("package:", "")
        packages.append(p)
        print(f"[{i}] {p}")

    print(f"[{len(packages)+1}] Manual")

    pilih_pkg = input("\nPilih : ")

    if pilih_pkg.isdigit():
        pilih_pkg = int(pilih_pkg)

        if 1 <= pilih_pkg <= len(packages):
            package = packages[pilih_pkg - 1]

        elif pilih_pkg == len(packages) + 1:
            package = input("Masukkan Package : ")

    print("\nPackage dipilih :", package)

    input("\nTekan ENTER untuk kembali...")
    elif pilih == "3":
        clear()
        print("=== UBAH LINK ===")
        link = input("Masukkan Link Roblox : ")

        print("\nLink berhasil diubah:")
        print(link)

        input("\nTekan ENTER untuk kembali...")

    elif pilih == "4":
        clear()
        print("=== PENGATURAN ===")

        delay = input("Delay (detik) : ")
        interval = input("Interval Cek (detik) : ")
        retry = input("Retry Maksimal : ")

        print("\nPengaturan tersimpan.")

        input("\nTekan ENTER untuk kembali...")

    elif pilih == "5":
        clear()
        print("=== LOG ===")
        print("Belum ada log.")

        input("\nTekan ENTER untuk kembali...")

    elif pilih == "6":
        print("\nTerima kasih telah menggunakan Roblox Rejoin V2.")
        break

    else:
        input("\nPilihan tidak valid! Tekan ENTER...")
