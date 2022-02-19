mkdir public
mkdir public/small
mkdir public/medium
mkdir public/large



echo "Working on large images"

for f in ../strapi.accords-library.com/public/uploads/*; do
    filename=$(basename "$f")
    ./cwebp -short -m 6 -q 80 -alpha_q 80 -mt -resize 0 2048 $f -o public/large/${filename%.*}.webp
done