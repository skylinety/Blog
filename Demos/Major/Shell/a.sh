a=1
echo "b is $b"
# b is 
BASEDIR=$(dirname "$0")
echo $BASEDIR
. "$BASEDIR/b.sh"
# a is 1
echo "b is $b"
# b is 2
source "$BASEDIR/b.sh"
# a is 1
sh "$BASEDIR/b.sh"
# a is
export a
sh "$BASEDIR/b.sh"
# a is 1