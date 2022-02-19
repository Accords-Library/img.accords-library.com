mkdir public
mkdir public/small
mkdir public/medium
mkdir public/large

echo "Working on small images"

for f in ../strapi.accords-library.com/public/uploads/*; do
    filename=$(basename "$f")
    ./cwebp -short -m 6 -q 60 -alpha_q 60 -mt -resize 0 512 $f -o public/small/${filename%.*}.webp
done

echo "Working on medium images"

for f in ../strapi.accords-library.com/public/uploads/*; do
    filename=$(basename "$f")
    ./cwebp -short -m 6 -q 75 -alpha_q 75 -mt -resize 0 1024 $f -o public/medium/${filename%.*}.webp
done

echo "Working on large images"

for f in ../strapi.accords-library.com/public/uploads/*; do
    filename=$(basename "$f")
    ./cwebp -short -m 6 -q 80 -alpha_q 80 -mt -resize 0 2048 $f -o public/large/${filename%.*}.webp
done