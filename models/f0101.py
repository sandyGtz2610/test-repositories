import cx_Oracle

class F0101Model:
	def __init__(self, an8, rfc):
		self.an8 = an8
		self.rfc = rfc

	def json(self):
		return {"an8" : self.an8, "rfc" : self.rfc}

	@classmethod
	def find_by_an8(cls, an8):
		#dns = cx_Oracle.makedns('10.192.8.35','1521','FANPY')
		connection = cx_Oracle.connect('CRPDTA/CRPDTA@10.192.8.35:1521/FANPY')
		cursor = connection.cursor()
		query = "SELECT ABAN8,ABTAX FROM CRPDTA.F0101 WHERE ABAN8= :an8"
		result = cursor.execute(query,{'an8': int(an8)})
		row = result.fetchone()
		connection.close()
		if row:
			return cls(row[0],row[1])