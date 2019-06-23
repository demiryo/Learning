#include "Riddle_form.h"

using namespace System;
using namespace System::Windows::Forms;

[STAThread]
void main(array<String^>^ args)
{
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);

	Riddle__Omar_demiry::Riddle_form form;
	Application::Run(%form);
}
