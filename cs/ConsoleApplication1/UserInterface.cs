using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
	class UserInterface
	{
		static string outputMenu(
			string[] messages)
		{
			Console.Clear();
			foreach (string message in messages)
			{
				Console.WriteLine(message);
			}
			Console.WriteLine("select a number and press enter");

			return Console.ReadLine();
		}


		public static float AskUserForNumber(string lable)
		{
			bool Error = true;
			float returnValue = 0;
			do
			{

				Console.Write("Enter your " + lable + " number:");
				string first = Console.ReadLine();
				// Check if something whent wrong then repeat previous step
				// If no error set Error = false;
				Error = !float.TryParse(first, out returnValue);
			} while (Error);
			return returnValue;
		}

		static void mathMenu()
		{
			string key;
			do
			{
				key = outputMenu(
					new string[] {
				"1. addition",
				"2. subtraction",
				"3. multiplacation",
				"4. divide",
				"5. exit" });

				if (key == "1")
				{
					// call add function
					MathFunctions.AddHandler();
				}
				if (key == "2")
				{
					MathFunctions.SubtractHandler();
				}
				if (key == "3")
				{
					MathFunctions.MultiplyHandler();
				}
				if (key == "4")
				{
					MathFunctions.DivideHandler();
				}
			} while (key != "5");
		}

		static void geometryMenu()
		{
			string key;
			do
			{
				key = outputMenu(
					new string[] {
				"1. triangles",
				"2. rectangle",
				"3. 3.D. shapes",
				"4. exit" });
			} while (key != "4"); // exit if we get a 4
		}

		public static void mainMenu()
		{
			string key;
			do
			{
				key = outputMenu(
					new string[] {
				"1. Math",
				"2. Geometry",
				"3. exit" });
				if (key == "1")
				{
					mathMenu();
				}
				if (key == "2")
				{
					geometryMenu();
				}
			} while (key != "3");
		}
	}
}
