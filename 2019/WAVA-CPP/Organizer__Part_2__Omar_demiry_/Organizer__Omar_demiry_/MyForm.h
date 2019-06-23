#include "AddItem.h"

#pragma once

namespace Organizer__Omar_demiry_ {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;
	using namespace System::Xml; 

	/// <summary>
	/// Summary for MyForm
	/// </summary>
	public ref class MyForm : public System::Windows::Forms::Form
	{
	public:
		MyForm(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}
	private: System::Windows::Forms::ToolStripMenuItem^  addNewItemToolStripMenuItem;
	public:
		DataSet^dslist;

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~MyForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::MenuStrip^  menuStrip1;
	protected:
	private: System::Windows::Forms::ToolStripMenuItem^  fileToolStripMenuItem;
	private: System::Windows::Forms::ToolStripMenuItem^  exitToolStripMenuItem;
	private: System::Windows::Forms::DataGridView^  MyGrid;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^  Book_name;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^  Genre;


	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->menuStrip1 = (gcnew System::Windows::Forms::MenuStrip());
			this->fileToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->addNewItemToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->exitToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->MyGrid = (gcnew System::Windows::Forms::DataGridView());
			this->Book_name = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			this->Genre = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			this->menuStrip1->SuspendLayout();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->MyGrid))->BeginInit();
			this->SuspendLayout();
			// 
			// menuStrip1
			// 
			this->menuStrip1->Items->AddRange(gcnew cli::array< System::Windows::Forms::ToolStripItem^  >(1) { this->fileToolStripMenuItem });
			this->menuStrip1->Location = System::Drawing::Point(0, 0);
			this->menuStrip1->Name = L"menuStrip1";
			this->menuStrip1->Size = System::Drawing::Size(484, 24);
			this->menuStrip1->TabIndex = 0;
			this->menuStrip1->Text = L"menuStrip1";
			// 
			// fileToolStripMenuItem
			// 
			this->fileToolStripMenuItem->DropDownItems->AddRange(gcnew cli::array< System::Windows::Forms::ToolStripItem^  >(2) {
				this->addNewItemToolStripMenuItem,
					this->exitToolStripMenuItem
			});
			this->fileToolStripMenuItem->Name = L"fileToolStripMenuItem";
			this->fileToolStripMenuItem->Size = System::Drawing::Size(35, 20);
			this->fileToolStripMenuItem->Text = L"file";
			this->fileToolStripMenuItem->Click += gcnew System::EventHandler(this, &MyForm::fileToolStripMenuItem_Click);
			// 
			// addNewItemToolStripMenuItem
			// 
			this->addNewItemToolStripMenuItem->Name = L"addNewItemToolStripMenuItem";
			this->addNewItemToolStripMenuItem->Size = System::Drawing::Size(150, 22);
			this->addNewItemToolStripMenuItem->Text = L"Add New Item";
			this->addNewItemToolStripMenuItem->Click += gcnew System::EventHandler(this, &MyForm::addNewItemToolStripMenuItem_Click);
			// 
			// exitToolStripMenuItem
			// 
			this->exitToolStripMenuItem->Name = L"exitToolStripMenuItem";
			this->exitToolStripMenuItem->Size = System::Drawing::Size(150, 22);
			this->exitToolStripMenuItem->Text = L"exit";
			this->exitToolStripMenuItem->Click += gcnew System::EventHandler(this, &MyForm::exitToolStripMenuItem_Click);
			// 
			// MyGrid
			// 
			this->MyGrid->AllowUserToAddRows = false;
			this->MyGrid->AllowUserToDeleteRows = false;
			this->MyGrid->AllowUserToResizeColumns = false;
			this->MyGrid->AllowUserToResizeRows = false;
			this->MyGrid->ColumnHeadersHeightSizeMode = System::Windows::Forms::DataGridViewColumnHeadersHeightSizeMode::AutoSize;
			this->MyGrid->Location = System::Drawing::Point(7, 27);
			this->MyGrid->Name = L"MyGrid";
			this->MyGrid->Size = System::Drawing::Size(465, 322);
			this->MyGrid->TabIndex = 1;
			// 
			// Book_name
			// 
			this->Book_name->HeaderText = L"Book_name";
			this->Book_name->Name = L"Book_name";
			// 
			// Genre
			// 
			this->Genre->HeaderText = L"Genre";
			this->Genre->Name = L"Genre";
			// 
			// MyForm
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::SystemColors::Control;
			this->ClientSize = System::Drawing::Size(484, 361);
			this->Controls->Add(this->MyGrid);
			this->Controls->Add(this->menuStrip1);
			this->ForeColor = System::Drawing::SystemColors::ControlText;
			this->MainMenuStrip = this->menuStrip1;
			this->Name = L"MyForm";
			this->StartPosition = System::Windows::Forms::FormStartPosition::WindowsDefaultBounds;
			this->Text = L"Omar\'s Organizer";
			this->Load += gcnew System::EventHandler(this, &MyForm::MyForm_Load);
			this->menuStrip1->ResumeLayout(false);
			this->menuStrip1->PerformLayout();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->MyGrid))->EndInit();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void fileToolStripMenuItem_Click(System::Object^  sender, System::EventArgs^  e) 
	{
		
	}
	
	private: System::Void exitToolStripMenuItem_Click(System::Object^  sender, System::EventArgs^  e) 
	{
		Close();
	}

	private: System::Void MyForm_Load(System::Object^  sender, System::EventArgs^  e) 
	{
		dslist = gcnew DataSet("list");
		this->dslist->ReadXml("Data.xml");
		this->MyGrid->DataSource = dslist;
		this->MyGrid->DataMember = "book";
	}
	private: System::Void addNewItemToolStripMenuItem_Click(System::Object^  sender, System::EventArgs^  e)
	{
		AddItem^AddItemWindow = gcnew AddItem();
		AddItemWindow->ShowDialog(); 
		this->dslist->Clear();
		this->dslist->ReadXml("Data.xml");
		this->MyGrid->DataMember = "book";

	}
};
}
