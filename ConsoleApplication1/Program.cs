using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
	class Program
	{
        static void MakeAGess()
        {
            Console.WriteLine(@"type any number");
            string input = Console.ReadLine();
            Console.WriteLine(@"time it by 5");
            string inputTimesFive = Console.ReadLine();


            int val = int.Parse(input);
            int answer = int.Parse(inputTimesFive);

            if (val * 5 == answer)
                Console.WriteLine(@"Correct! good for you!= (");
            else
                Console.WriteLine(@"horribile! are you egyptian!= )");
        }

		static void AnnoyingBanana()
		{
			Console.WriteLine("hi i like bananas! what do u think?");

			for (int i = 0; i < 20; i = i + 2)
			{
				string message = Console.ReadLine();
				Console.WriteLine("Loop no. " + i.ToString() + " : " + message + " respond!");
			}

			// Wait for any key
			Console.WriteLine("type to escape ebiss...");
			Console.ReadLine();
			// wait for 3 minutes then respond.
			Console.WriteLine(" O.K.i won't let u out. >= )");
		}

		static string outputmenu()
		{
			Console.Clear();
            Console.WriteLine("1. addition");
			Console.WriteLine("2. subtraction");
			Console.WriteLine("3. multiplacation");
			Console.WriteLine("4. divide");
			Console.WriteLine("5. exit");
			Console.WriteLine("select a number and press enter");
           
				return Console.ReadLine();
		}

		static void AddHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to add!");

			float first = AskUserForNumber("first");
			float second = AskUserForNumber("second");

			Console.Write(String.Format("{0} + {1} = {2}", first, second, first + second));
			Console.ReadKey();
        }
		static void SubtractHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to sub!");

			float first = AskUserForNumber("first");
			float second = AskUserForNumber("second");

			Console.Write(String.Format("{0} - {1} = {2}", first, second, first - second));
			Console.ReadKey();
		}
		static void MultiplyHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to times!");

			float first = AskUserForNumber("first");
			float second = AskUserForNumber("second");

			Console.Write(String.Format("{0} x {1} = {2}", first, second, first * second));
			Console.ReadKey();
		}
		static void DivideHandler()
		{
			Console.Clear();
			Console.WriteLine("Welcome to divide!");

			float first = AskUserForNumber("first");
			float second = AskUserForNumber("second");

			Console.Write(String.Format("{0} / {1} = {2}", first, second, first / second));
			Console.ReadKey();
		}
		static float AskUserForNumber(string lable)
		{
			bool Error = true;
			float returnValue = 0;
			do
			{

				Console.Write("Enter your "+lable+" number:");
				string first = Console.ReadLine();
				// Check if something whent wrong then repeat previous step
				// If no error set Error = false;
				Error = !float.TryParse(first, out returnValue);
            } while (Error);
			return returnValue;
        }

		static void Main(string[] args)
		{
			string key;
			do {
				key = outputmenu();

				if (key == "1")
				{
					// call add function
					AddHandler();
				}
				if (key == "2")
				{
					SubtractHandler();
                }
				if (key == "3")
				{
					MultiplyHandler();
				}
				if (key == "4")
				{
					DivideHandler();
				}
			} while (key != "5");
		}
	}
}
