BASEDIR=$(dirname "$0")
echo $BASEDIR
# /Users/skyline/Workspace/skyline/Blog/Demos/Major/Shell

a=1
echo "b is $b"
# b is 
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