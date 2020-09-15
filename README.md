# mllogdp

for name in *.mol; do  echo "babel --gen3D -imol "$name" -omol new_"$name" ; mv  new_"$name $name ; done> commands.sh

cat commands.sh | parallel -P 16 > log 2> error.log

