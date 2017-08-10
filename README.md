<h2 align="center">conexion LDAP de active directory con Django</h2>







se instaló 
ldap3==2.2.2
pyldap==2.4.35.1
Django==1.11.4
django-auth-ldap==1.2.14



variables de configuracion en el settings.py 

import ldap, logging
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

AUTH_LDAP_SERVER_URI = "ldap://mysite.edu.co"
AUTH_LDAP_BIND_DN = "CN=Automata Auth,CN=pseudo,CN=Usuarios,DC=mysite,DC=edu,DC=co"
AUTH_LDAP_BIND_PASSWORD = "MyPassWord"
AUTH_LDAP_USER_SEARCH = LDAPSearch("CN=pseudo,CN=Usuarios,DC=mysite,DC=edu,DC=co",ldap.SCOPE_SUBTREE, "(samAccountName=%(user)s)")

AUTHENTICATION_BACKENDS = (
'django_auth_ldap.backend.LDAPBackend',
'django.contrib.auth.backends.ModelBackend',
)

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}



se hizo uso de:
Apache directory studio para buscar la informacion dentro del AD


enlaces de interes: 
http://www.kouti.com/tables/userattributes.htm
https://msdn.microsoft.com/en-us/library/ms675090(v=vs.85).aspx
https://docs.djangoproject.com/en/1.11/ref/contrib/auth/

