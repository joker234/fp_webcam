# Usage-examples:
#
# 1. test random
# source testmove.sh
# movecam
#
# 2. test random in loop
# source testmove.sh
# for i in {0..20}; do
# 	movecam
# done
#
# 3. test with temporairly other ip
# source testmove.sh
# raspiip="10.0.0.8" movecam
#
# 4. test with fixed direction
# source testmove.sh
# dire="down" movecam

function movecam() {
	if ! (($+raspiip)) {
		raspiip="192.168.0.16"
	}
	base_url="http://${raspiip}:8090?dire="

	if ! (($+dire)) {
		a=$[RANDOM % 4]
		case $a in
			0)
				b=up
				;;
			1)
				b=down
				;;
			2)
				b=left
				;;
			3)
				b=right
				;;
			*)
				echo "This should never occur. You're such a bad guy"
				;;
		esac
	} else {
		b=$dire
	}

	echo "going $b using \"${base_url}${b}\""
	curl "${base_url}${b}" -s >/dev/null
}
