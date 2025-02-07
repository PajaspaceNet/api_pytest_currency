# API Pytest Currency 💰

Tento projekt umožňuje **konverzi měn** pomocí API a obsahuje **automatické testy** pomocí `pytest`.

## 🚀 Jak spustit projekt?

### 1️⃣ Klonování repozitáře
Naklonuj repozitář na svůj počítač:
```sh
git clone https://github.com/PajaspaceNet/api_pytest_currency.git
cd api_pytest_currency
```

### 2️⃣ Vytvoření a aktivace virtuálního prostředí
Doporučujeme spustit projekt v **virtuálním prostředí**:
```sh
python -m venv venv
```
- **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```

### 3️⃣ Instalace závislostí
```sh
pip install -r requirements.txt
```

### 4️⃣ Spuštění aplikace
```sh
python converter.py
```

## 🛠️ Jak spustit testy?
Testy jsou napsané v `pytest`. Spusť je tímto příkazem:
```sh
pytest test_converter.py
```

## 📚 Technologie
- **Python** 🐍
- **Requests** 🌍 (pro práci s API)
- **Pytest** ✅ (testování)

## 🐝 Licence
Tento projekt je open-source pod licencí **MIT**.

