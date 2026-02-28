import pandas as pd
from pandera.pandas import DataFrameSchema, Column
import pytest


@pytest.fixture
def datos_banco():
    """Fixture para cargar los datos del banco desde un archivo csv
    Returns:
        pd.Dataframe: DatFrame que contiene los datos del banco.
    """
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep = ';')
    return df

def test_esquema(datos_banco):
    """Test de esquema para el DataFrame de datos_banco.

    Args:
        datos_banco (pd.Datframe): DataFrame que contiene los datos del banco.
    """
    df = datos_banco
    esquema = DataFrameSchema ({
        "age": Column (int, nullable=False),
        "job": Column (str, nullable=False),
        "marital": Column (str, nullable=False),
        "education": Column (str, nullable=False),
        "default": Column (str, nullable=False),
        "housing": Column (str, nullable=False),
        "loan": Column (str, nullable=False),
        "contact": Column (str, nullable=False),
        "month": Column (str, nullable=False),
        "day_of_week": Column (str, nullable=False),
        "duration": Column (int, nullable=False),
        "campaign": Column (int, nullable=False),
        "pdays": Column (int, nullable=False),
        "previous": Column (int, nullable=False),
        "poutcome": Column (str, nullable=False),
        "emp.var.rate": Column (float, nullable=False),
        "cons.price.idx": Column (float, nullable=False),
        "euribor3m": Column (float, nullable=False),
        "nr.employed": Column (float, nullable=False),
        "y": Column (str, nullable=False)
    })

    esquema.validate(df)

def test_basico(datos_banco):
        """Test básico para verificar que el DataFrame de datos_banco no está vacío y contiene las columnas esperadas.

        Args:
            datos_banco (pd.DataFrame): DataFrame que contiene los datos del banco.
        """
        df = datos_banco

        # Verificar que el DataFrame no está vacío
        assert not df.empty, "El DataFrame está vacío"

        #Verificar nulos
        assert df.isnull().sum().sum() == 0, "El DataFrame contiene valores nulos"

        #Verificar cantidad de columnas
        assert df.shape[1] == 21, f"El DataFrame debería tener 21 columnas, pero tiene {df.shape[1]}"   

def test_adicional(datos_banco):
        """Test para verificar que no existan columnas duplicadas en el DataFrame

        Args:
            datos_banco (pd.DataFrame): DataFrame que contiene los datos del banco.
        """
        df = datos_banco

        
        
        duplicates = df.columns[df.columns.duplicated()] 
        assert len(duplicates) == 0, f"El DataFrame contiene columnas duplicadas: {list(duplicates)}"