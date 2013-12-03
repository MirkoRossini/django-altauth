USER=user
SERVER_PATH="localhost:8000"
COOKIE_PATH=/tmp/cookies.txt

data=$(curl -s -c $COOKIE_PATH http://$SERVER_PATH/accounts/login/ | grep -o "name=['\"]csrfmiddlewaretoken['\"] value=['\"][^'\"]*" | sed -e "s/name='//" -e "s/'\s*value='/=/")\&username=$USER

token=`curl -b $COOKIE_PATH -c $COOKIE_PATH -d $data -X POST -H 'Content-Type: application/x-www-form-urlencoded' http://$SERVER_PATH/altauth/get_public_key_token/  | python -m altauth.utils decrypt_rsa -p ~/.ssh/id_rsa` 

curl -b $COOKIE_PATH -c $COOKIE_PATH -d "$data&token=$token"  -X POST -H 'Content-Type: application/x-www-form-urlencoded' http://$SERVER_PATH/altauth/public_key_login/


# User is now logged in, use curl with cookies from now on
