#include "MyForm.h"
using namespace System;
using namespace System::Windows::Forms;

[STAThread]
void main(array<String^>^ args)
{

	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);

	Organizer__Omar_demiry_::MyForm form;
	Application::Run(%form);
}
