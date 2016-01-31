using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
	class MathFunctions
	{
		public static void AddHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to add!");

			float first = UserInterface.AskUserForNumber("first");
			float second = UserInterface.AskUserForNumber("second");

			Console.Write(String.Format("{0} + {1} = {2}", first, second, first + second));
			Console.ReadKey();
		}
		public static void SubtractHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to sub!");

			float first = UserInterface.AskUserForNumber("first");
			float second = UserInterface.AskUserForNumber("second");

			Console.Write(String.Format("{0} - {1} = {2}", first, second, first - second));
			Console.ReadKey();
		}
		public static void MultiplyHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to times!");

			float first = UserInterface.AskUserForNumber("first");
			float second = UserInterface.AskUserForNumber("second");

			Console.Write(String.Format("{0} x {1} = {2}", first, second, first * second));
			Console.ReadKey();
		}
		public static void DivideHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to divide!");

			float first = UserInterface.AskUserForNumber("first");
			float second = UserInterface.AskUserForNumber("second");

			Console.Write(String.Format("{0} / {1} = {2}", first, second, first / second));
			Console.ReadKey();
		}
	}
}
