# mysql
select firstname, lastname, city, state
from Person as pers
left join Address as addr on pers.PersonId = addr.PersonId
