#!/bin/bash

echo "program percabangan sederhana aritmatika"
printf "1. penjumlahan\n"
printf "2. pengurangan\n"
printf "3. pembagian\n"
printf "4. perkalian\n"
printf "5. modular\n"

echo "pilih salah satu program aritmatika diatas  1/2/3/4/5"

read pilih

case "$pilih" in
	"1")
	echo "---Penjumlahan---"
	echo "masukkan nilai pertama"
	read a
	echo "masukkan nilai kedua"
	read b
	let hasil=$a+$b
	echo "hasilnya = $hasil"
	 ;;
	"2")
        echo "---Pengurangan---"
        echo "masukkan nilai pertama"
        read a
        echo "masukkan nilai kedua"
        read b
        let hasil=$a-$b
        echo "hasilnya = $hasil"
         ;;
	"3")
	echo "---Pembagian---"
        echo "masukkan nilai pertama"
        read a
        echo "masukkan nilai kedua"
        read b
        let hasil=$a/$b
        echo "hasilnya = $hasil"
         ;;
        "4")
        echo "---Perkalian---"
        echo "masukkan nilai pertama"
        read a
        echo "masukkan nilai kedua"
        read b
        let hasil=$a*$b
        echo "hasilnya = $hasil"
         ;;
        "5")
        echo "---modular---"
        echo "masukkan nilai pertama"
        read a
        echo "masukkan nilai kedua"
        read b
        let hasil=$a%$b
        echo "hasilnya = $hasil"
         ;;
	esac
