using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void DrawHeart(Graphics g)
		{
			var orgState = g.Save();
			g.TranslateTransform(100, 100);
			g.RotateTransform(45);
			g.DrawArc(Pens.Red, 0, 0, 45, 100, -135, 180);
			g.RotateTransform(-45);
			g.TranslateTransform(-37, 0);
			g.RotateTransform(-45);
			g.ScaleTransform(-1, 1);
			g.DrawArc(Pens.Red, 0, 0, 45, 100, -135, 180);
			g.Restore(orgState);
		}
		private void Form1_Paint(object sender, PaintEventArgs e)
		{
			DrawHeart(e.Graphics);
		}
	}
}
