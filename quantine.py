import sqlite3
from sqlite3 import Error


class QuantineSQL:
  _create_table_providers = """
  CREATE TABLE Providers (
    ProviderId   INTEGER PRIMARY KEY AUTOINCREMENT,
    ProviderName VARCHAR(128) NOT NULL
  );
  """

  _create_table_canteens = """
  CREATE TABLE Canteens (
    CanteenId  integer PRIMARY KEY AUTOINCREMENT,
    Name       VARCHAR(128) NOT NULL,
    Location   VARCHAR(128) NOT NULL,
    TimeOpen   VARCHAR      NOT NULL,
    TimeClosed VARCHAR      NOT NULL,
    ProviderId INTEGER      NOT NULL,
    FOREIGN KEY (ProviderId) REFERENCES Providers (ProviderId) ON DELETE CASCADE
  );
  """
  _insert_providers = """
  INSERT INTO Providers (ProviderName)
  VALUES ('Rahva Toit'),
       ('Baltic Restaurants Estonia AS'),
       ('TTÜ Sport OÜ'),
       ('BitStop OÜ');
  """

  _insert_canteens = """
  INSERT INTO Canteens (Name, Location, ProviderId, TimeOpen, TimeClosed)
  VALUES ('SOC: building', 'Akadeemia tee 3', 1, '08:30', '18:30'),
       ('Libary canteen', 'Akadeemia tee 1/Ehitajate tee 7', 1, '08:30', '19:00'),
       ('Main building Deli cafe', 'Ehitajate tee 5', 2, '09:00', '19:00'),
       ('Main building Daily lunch restaurant', 'Ehitajate tee 5', 2, '9:00', '16:00'),
       ('U06 building canteen', 'Ehitajate tee 5', 1, '09:00', '16:00'),
       ('Natural Science building canteen', 'Akadeemia tee 15', 2, '9:00', '16:00'),
       ('ICT building canteen', 'Raja 15/Mäepealse 1', 2, '09:00', '16:00'),
       ('Sports building canteen', 'Männiliiva 7', 3, '11:00', '20:00');
  """

  _insert_bitStop = """
  INSERT INTO Canteens (Name, Location, ProviderId, TimeOpen, TimeClosed)
  VALUES ('bitStop Kohvik', 'RAJA 4C', 4, '09:30', '16:00');
  """

  _get_canteens_between = """
  SELECT Name, Location, TimeOpen, TimeClosed
  FROM Canteens
  WHERE TimeClosed >= '18:00' AND TimeOpen <= '16:15';
  """

  _get_rahva_toit = """
  SELECT Name, Location, TimeOpen, TimeClosed, p.ProviderName
  FROM Canteens
          LEFT JOIN Providers P on Canteens.ProviderId = P.ProviderId
  WHERE p.ProviderName = 'Rahva Toit';
  """

  def __init__(self, path):
    """Constructor. Accepts database file path as an argument."""
    self.connection = self.create_connection(path)
    self.cursor = self.connection.cursor()

  def create_connection(self, path):
    """Initialize the connection to the database."""
    try:
        return sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

  def execute_query(self, query):
    """Generic method for creating tables."""
    try:
        self.cursor.execute(query)
        self.connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

  def create_canteen_tables(self):
    return self.execute_query(self._create_table_canteens)

  def create_provider_tables(self):
    return self.execute_query(self._create_table_providers)

  def insert_canteens(self):
    return self.execute_query(self._insert_canteens)

  def insert_providers(self):
    return self.execute_query(self._insert_providers)

  def insert_bitstop(self):
    return self.execute_query(self._insert_bitStop)

  def execute_read_query(self, query):
    """Generic read method for getting data."""
    try:
      self.cursor.execute(query)
      return self.cursor.fetchall()
    except expression as identifier:
      print(f"The error '{e}' occurred") 

  def get_canteens_form_four_fifteet_to_six_pm(self):
    return self.execute_read_query(self._get_canteens_between)

  def get_canteens_ran_by_rahva_toit(self):
    return self.execute_read_query(self._get_rahva_toit)

  def execute_all_write_methods(self):
    self.create_provider_tables()
    self.create_canteen_tables()
    self.insert_providers()
    self.insert_canteens()
    self.insert_bitstop()


if __name__ == "__main__":
  db_connection = QuantineSQL("canteen.db")
  # db_connection.execute_all_write_methods() # Only run once to insert data anc create table
  canteens_by_rahva_toit = db_connection.get_canteens_ran_by_rahva_toit()
  canteen_by_time = db_connection.get_canteens_form_four_fifteet_to_six_pm()

  print("-- 3) Create query for canteens which are open 16.15:18.00")
  for i, canteen in enumerate(canteens_by_rahva_toit):
    print(f"{i}) Building: {canteen[0]}, Address: {canteen[1]},  Opening Time: {canteen[2]}, Closing Time: {canteen[3]}")

  print("-- 4) Create query for canteens which are serviced by Rahva Toit")

  for i, canteen in enumerate(canteen_by_time):
    print(f"{i}) Building: {canteen[0]}, Address: {canteen[1]},  Opening Time: {canteen[2]}, Closing Time: {canteen[3]}")
  