-- 1) Create SQLite database DINERS, with two related tables CANTEEN and PROVIDER

CREATE TABLE Providers
(
    ProviderId   INTEGER PRIMARY KEY AUTOINCREMENT,
    ProviderName VARCHAR(128) NOT NULL
);


CREATE TABLE Canteens
(
    CanteenId  integer PRIMARY KEY AUTOINCREMENT,
    Name       VARCHAR(128) NOT NULL,
    Location   VARCHAR(128) NOT NULL,
    TimeOpen   VARCHAR      NOT NULL,
    TimeClosed VARCHAR      NOT NULL,
    ProviderId INTEGER      NOT NULL,
    FOREIGN KEY (ProviderId) REFERENCES Providers (ProviderId) ON DELETE CASCADE
);

-- Create a index
CREATE INDEX CanteensProvider ON Canteens(ProviderId);

-- 2) Insert IT College canteen data by separate statement, other canteens as one list.
INSERT INTO Providers (ProviderName)
VALUES ('Rahva Toit'),
       ('Baltic Restaurants Estonia AS'),
       ('TTÜ Sport OÜ'),
       ('BitStop OÜ');

INSERT INTO Canteens (Name, Location, ProviderId, TimeOpen, TimeClosed)
VALUES ('SOC: building', 'Akadeemia tee 3', 1, '08:30', '18:30'),
       ('Libary canteen', 'Akadeemia tee 1/Ehitajate tee 7', 1, '08:30', '19:00'),
       ('Main building Deli cafe', 'Ehitajate tee 5', 2, '09:00', '19:00'),
       ('Main building Daily lunch restaurant', 'Ehitajate tee 5', 2, '9:00', '16:00'),
       ('U06 building canteen', 'Ehitajate tee 5', 1, '09:00', '16:00'),
       ('Natural Science building canteen', 'Akadeemia tee 15', 2, '9:00', '16:00'),
       ('ICT building canteen', 'Raja 15/Mäepealse 1', 2, '09:00', '16:00'),
       ('Sports building canteen', 'Männiliiva 7', 3, '11:00', '20:00');


INSERT INTO Canteens (Name, Location, ProviderId, TimeOpen, TimeClosed)
VALUES ('bitStop Kohvik', 'RAJA 4C', 4, '09:30', '16:00');


-- SELECT  * FROM Canteens;
-- 3) Create query for canteens which are open 16.15:18.00
SELECT Name, Location, TimeOpen, TimeClosed
FROM Canteens
WHERE TimeClosed >= '18:00'
  AND TimeOpen <= '16:15';

-- 4) Create query for canteens which are serviced by Rahva Toit
SELECT Name, Location, TimeOpen, TimeClosed, p.ProviderName
FROM Canteens
         LEFT JOIN Providers P on Canteens.ProviderId = P.ProviderId
WHERE p.ProviderName = 'Rahva Toit';
