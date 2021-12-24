import EX1_funcs
import unittest

class EX1FuncsTestCase(unittest.TestCase):

	def test_min(self):
		self.assertEqual(EX1_funcs.min(0,2),0)
		self.assertEqual(EX1_funcs.min(-1,-5),-5)
		self.assertEqual(EX1_funcs.min(-1,2),-1)
		self.assertEqual(EX1_funcs.min(0,0),0)

	def test_mean(self):
		self.assertEqual(EX1_funcs.mean([1,2,3,4,5]),3)
		self.assertEqual(EX1_funcs.mean([-4,3,0,-2,2]),-0.2)
		self.assertEqual(EX1_funcs.mean([12]),12)
		self.assertEqual(EX1_funcs.mean([]),None)

	def test_median(self):
		self.assertEqual(EX1_funcs.median([]),None)
		self.assertEqual(EX1_funcs.median([12]),12)
		self.assertEqual(EX1_funcs.median([-1,1]),0)
		self.assertEqual(EX1_funcs.median([-5,-8,6,0,-3,1]),-1.5)
		self.assertEqual(EX1_funcs.median([1,6,5,0,0,2,5]),2)

	def test_std_deviation(self):
		self.assertEqual(EX1_funcs.std_deviation([]),None)
		self.assertAlmostEqual(EX1_funcs.std_deviation([-3,2,5,0,0,2,18]),6.366365,places=5)
		self.assertEqual(EX1_funcs.std_deviation([12]),0)
		self.assertEqual(EX1_funcs.std_deviation([-42,-42]),0)
		self.assertEqual(EX1_funcs.std_deviation([-2,2]),2)
		self.assertEqual(EX1_funcs.std_deviation([0,0,0,0,213]),85.2)

	def test_is_arith_progression(self):
		self.assertEqual(EX1_funcs.is_arith_progression([]),None)
		self.assertEqual(EX1_funcs.is_arith_progression([12]),True)
		self.assertEqual(EX1_funcs.is_arith_progression([-2,0,2,4,4]),False)
		self.assertEqual(EX1_funcs.is_arith_progression([1,1,1]),True)
		self.assertEqual(EX1_funcs.is_arith_progression([1,12,23,34]),True)
		self.assertEqual(EX1_funcs.is_arith_progression([6,3,0,-3]),True)

	# By convention, common ratio can't be equal to 0
	def test_is_geo_progression(self):
		self.assertEqual(EX1_funcs.is_geo_progression([]),None)
		self.assertEqual(EX1_funcs.is_geo_progression([0,0,0]),False)
		self.assertEqual(EX1_funcs.is_geo_progression([2]),True)
		self.assertEqual(EX1_funcs.is_geo_progression([-2,-6,-18,-54]),True)
		self.assertEqual(EX1_funcs.is_geo_progression([1,-1,1,-1]),True)
		self.assertEqual(EX1_funcs.is_geo_progression([1,-2,4,-8]),True)
		self.assertEqual(EX1_funcs.is_geo_progression([1,3,5,7]),False)
		self.assertEqual(EX1_funcs.is_geo_progression([12,0,0,0]),False)

	def test_next_arith_progression(self):
		self.assertEqual(EX1_funcs.next_arith_progression(12,[]),(None,None))
		self.assertEqual(EX1_funcs.next_arith_progression(0,[12]),(True,[]))		
		self.assertEqual(EX1_funcs.next_arith_progression(1,[12]),(True,[12]))
		self.assertEqual(EX1_funcs.next_arith_progression(0,[-2,0,2,4,4]),(False,[]))		
		self.assertEqual(EX1_funcs.next_arith_progression(3,[-2,0,2,4,4]),(False,[]))
		self.assertEqual(EX1_funcs.next_arith_progression(0,[1,1,1]),(True,[]))		
		self.assertEqual(EX1_funcs.next_arith_progression(2,[1,1,1]),(True,[1,1]))
		self.assertEqual(EX1_funcs.next_arith_progression(0,[1,12,23,34]),(True,[]))		
		self.assertEqual(EX1_funcs.next_arith_progression(4,[1,12,23,34]),(True,[45,56,67,78]))
		self.assertEqual(EX1_funcs.next_arith_progression(0,[6,3,0,-3]),(True,[]))		
		self.assertEqual(EX1_funcs.next_arith_progression(1,[6,3,0,-3]),(True,[-6]))

	def test_next_geo_progression(self):
		self.assertEqual(EX1_funcs.next_geo_progression(12,[]),(None,None))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[0,0,0]),(False,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(1,[0,0,0]),(False,[]))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[2]),(True,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(3,[2]),(True,[2,2,2]))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[-2,-6,-18,-54]),(True,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(2,[-2,-6,-18,-54]),(True,[-162,-486]))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[1,-1,1,-1]),(True,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(4,[1,-1,1,-1]),(True,[1,-1,1,-1]))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[1,-2,4,-8]),(True,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(5,[1,-2,4,-8]),(True,[16,-32,64,-128,256]))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[1,3,5,7]),(False,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(2,[1,3,5,7]),(False,[]))
		self.assertEqual(EX1_funcs.next_geo_progression(0,[12,0,0,0]),(False,[]))		
		self.assertEqual(EX1_funcs.next_geo_progression(3,[12,0,0,0]),(False,[]))


if __name__ == '__main__':
	unittest.main()