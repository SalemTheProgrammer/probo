from itsdangerous import URLSafeTimedSerializer

def generate_reset_token(email, secret_key, salt, expiration=1800):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(email, salt=salt)

def confirm_reset_token(token, secret_key, salt, expiration=1800):
    serializer = URLSafeTimedSerializer(secret_key)
    try:
        email = serializer.loads(token, salt=salt, max_age=expiration)
    except:
        return False
    return email
