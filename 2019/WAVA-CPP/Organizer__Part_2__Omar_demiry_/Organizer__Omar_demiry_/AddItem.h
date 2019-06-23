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
	/// Summary for AddItem
	/// </summary>
	public ref class AddItem : public System::Windows::Forms::Form
	{
	public:
		AddItem(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~AddItem()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::TextBox^  txtItem_name;
	private: System::Windows::Forms::Label^  Label1;
	private: System::Windows::Forms::TextBox^  txtGenre;

	private: System::Windows::Forms::Label^  label2;

	private: System::Windows::Forms::Label^  label3;
	private: System::Windows::Forms::Button^  btnADD;
	private: System::Windows::Forms::Button^  btnCancel;
	private: System::Windows::Forms::TextBox^  txtYear;

	private: System::Windows::Forms::Label^  label4;
	private: System::Windows::Forms::TextBox^  txtPages;
	private: System::Windows::Forms::Label^  label5;


	protected:


	protected:

	protected:

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
			this->txtItem_name = (gcnew System::Windows::Forms::TextBox());
			this->Label1 = (gcnew System::Windows::Forms::Label());
			this->txtGenre = (gcnew System::Windows::Forms::TextBox());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->btnADD = (gcnew System::Windows::Forms::Button());
			this->btnCancel = (gcnew System::Windows::Forms::Button());
			this->txtYear = (gcnew System::Windows::Forms::TextBox());
			this->label4 = (gcnew System::Windows::Forms::Label());
			this->txtPages = (gcnew System::Windows::Forms::TextBox());
			this->label5 = (gcnew System::Windows::Forms::Label());
			this->SuspendLayout();
			// 
			// txtItem_name
			// 
			this->txtItem_name->Location = System::Drawing::Point(120, 64);
			this->txtItem_name->Name = L"txtItem_name";
			this->txtItem_name->Size = System::Drawing::Size(109, 20);
			this->txtItem_name->TabIndex = 0;
			// 
			// Label1
			// 
			this->Label1->AutoSize = true;
			this->Label1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 11.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->Label1->Location = System::Drawing::Point(12, 66);
			this->Label1->Name = L"Label1";
			this->Label1->Size = System::Drawing::Size(96, 18);
			this->Label1->TabIndex = 1;
			this->Label1->Text = L"Book_Name:";
			// 
			// txtGenre
			// 
			this->txtGenre->Location = System::Drawing::Point(120, 103);
			this->txtGenre->Name = L"txtGenre";
			this->txtGenre->Size = System::Drawing::Size(108, 20);
			this->txtGenre->TabIndex = 2;
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 11.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label2->Location = System::Drawing::Point(55, 105);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(53, 18);
			this->label2->TabIndex = 3;
			this->label2->Text = L"Genre:";
			// 
			// label3
			// 
			this->label3->AutoSize = true;
			this->label3->Location = System::Drawing::Point(30, 146);
			this->label3->Name = L"label3";
			this->label3->Size = System::Drawing::Size(0, 13);
			this->label3->TabIndex = 5;
			// 
			// btnADD
			// 
			this->btnADD->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 11.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->btnADD->Location = System::Drawing::Point(135, 266);
			this->btnADD->Name = L"btnADD";
			this->btnADD->Size = System::Drawing::Size(94, 32);
			this->btnADD->TabIndex = 6;
			this->btnADD->Text = L"Add";
			this->btnADD->UseVisualStyleBackColor = true;
			this->btnADD->Click += gcnew System::EventHandler(this, &AddItem::btnADD_Click);
			// 
			// btnCancel
			// 
			this->btnCancel->DialogResult = System::Windows::Forms::DialogResult::Cancel;
			this->btnCancel->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 11.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->btnCancel->Location = System::Drawing::Point(23, 266);
			this->btnCancel->Name = L"btnCancel";
			this->btnCancel->Size = System::Drawing::Size(85, 32);
			this->btnCancel->TabIndex = 7;
			this->btnCancel->Text = L"Cancel";
			this->btnCancel->UseVisualStyleBackColor = true;
			this->btnCancel->Click += gcnew System::EventHandler(this, &AddItem::btnCancel_Click);
			// 
			// txtYear
			// 
			this->txtYear->Location = System::Drawing::Point(120, 141);
			this->txtYear->Name = L"txtYear";
			this->txtYear->Size = System::Drawing::Size(109, 20);
			this->txtYear->TabIndex = 8;
			// 
			// label4
			// 
			this->label4->AutoSize = true;
			this->label4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 11.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label4->Location = System::Drawing::Point(66, 143);
			this->label4->Name = L"label4";
			this->label4->Size = System::Drawing::Size(42, 18);
			this->label4->TabIndex = 9;
			this->label4->Text = L"Year:";
			// 
			// txtPages
			// 
			this->txtPages->Location = System::Drawing::Point(120, 180);
			this->txtPages->Name = L"txtPages";
			this->txtPages->Size = System::Drawing::Size(108, 20);
			this->txtPages->TabIndex = 10;
			// 
			// label5
			// 
			this->label5->AutoSize = true;
			this->label5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 11.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->label5->Location = System::Drawing::Point(60, 182);
			this->label5->Name = L"label5";
			this->label5->Size = System::Drawing::Size(54, 18);
			this->label5->TabIndex = 11;
			this->label5->Text = L"Pages:";
			// 
			// AddItem
			// 
			this->AcceptButton = this->btnADD;
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->CancelButton = this->btnCancel;
			this->ClientSize = System::Drawing::Size(304, 330);
			this->Controls->Add(this->label5);
			this->Controls->Add(this->txtPages);
			this->Controls->Add(this->label4);
			this->Controls->Add(this->txtYear);
			this->Controls->Add(this->btnCancel);
			this->Controls->Add(this->btnADD);
			this->Controls->Add(this->label3);
			this->Controls->Add(this->label2);
			this->Controls->Add(this->txtGenre);
			this->Controls->Add(this->Label1);
			this->Controls->Add(this->txtItem_name);
			this->Name = L"AddItem";
			this->Text = L"Add New Book";
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion

	private: System::Void btnADD_Click(System::Object^  sender, System::EventArgs^  e)
	{
		XmlDocument^Data = gcnew XmlDocument();
		Data->Load("Data.xml");
		XmlElement^NewBook = Data->CreateElement("book");
		NewBook->SetAttribute("book_name", this->txtItem_name->Text);
		NewBook->SetAttribute("Genre", this->txtGenre->Text);
		NewBook->SetAttribute("year", this->txtYear->Text);
		NewBook->SetAttribute("pages", this->txtPages->Text);
		Data->DocumentElement->AppendChild(NewBook);
		Data->Save("Data.xml");

		Close();
	}
	private: System::Void btnCancel_Click(System::Object^  sender, System::EventArgs^  e) 
	{
		Close();

	}


};
}
