# bank_account.py

class Account:
    def __init__(self, account_number: str, account_holder: str, account_balance: float = 0.0):
        # 2) Définir les attributs
        self.account_number = account_number  # Numéro de compte (chaîne)
        self.account_balance = account_balance  # Solde du compte (flottant)
        self.account_holder = account_holder  # Titulaire du compte (chaîne)

    def deposit(self, amount: float):
        # 3) Méthode pour déposer de l'argent
        if amount > 0:
            self.account_balance += amount
            print(f"Dépôt de {amount} effectué. Nouveau solde: {self.account_balance}")
        else:
            print("Le montant à déposer doit être positif.")

    def withdraw(self, amount: float):
        # 4) Méthode pour retirer de l'argent
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Retrait de {amount} effectué. Nouveau solde: {self.account_balance}")
            else:
                print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            print("Le montant à retirer doit être positif.")

    def check_balance(self) -> float:
        # 5) Méthode pour vérifier le solde
        return self.account_balance


# 6) Créer une instance de la classe Account
my_account = Account(account_number="123456", account_holder="Alice")

# 7) Utiliser les méthodes pour déposer et retirer de l'argent et vérifier le solde
my_account.deposit(100.0)         # Dépôt de 100
my_account.withdraw(50.0)         # Retrait de 50
print(f"Solde actuel: {my_account.check_balance()}")  # Vérification du solde

# Tester avec une autre instance
another_account = Account(account_number="654321", account_holder="Bob", account_balance=200.0)
another_account.deposit(150.0)    # Dépôt de 150 sur le compte de Bob
another_account.withdraw(100.0)    # Retrait de 100 sur le compte de Bob
print(f"Solde actuel de Bob: {another_account.check_balance()}")  # Vérification du solde de Bob

# Essayer un retrait avec des fonds insuffisants
another_account.withdraw(300.0)    # Tentative de retrait de 300 sur le compte de Bob