class UserDomain:
    def __init__(self, name, email, password, celular=None, cnpj=None, active=False, activation_code=None):
        self.name = name
        self.email = email
        self.password = password
        self.celular = celular
        self.cnpj = cnpj
        self.active = active
        self.activation_code = activation_code

    def to_dict(self):
        """Retorna os dados do usuário sem expor a senha"""
        return {
            "name": self.name,
            "email": self.email,
            "celular": self.celular,
            "cnpj": self.cnpj,
            "active": self.active
        }