#include<iostream>

using namespace std;

int main(){

   
    const float price_middle_quality = 35.5;
    const float price_high_quality = 55.5;
    const int budget_valid_days = 30;
    float meters;
    float taxes;
    float middle_quality;
    float high_quality;
    float budget_middle_quality;
    float budget_high_quality;

    cout << "Inserte los metros de suelo a instalar: ";
    cin >> meters;
    cout << "IVA: ";
    cin >> taxes;

    middle_quality = meters * price_middle_quality;
    high_quality = meters * price_high_quality;
    
    budget_high_quality = high_quality * (taxes/100) + high_quality;
    budget_middle_quality = middle_quality * (taxes/100) + middle_quality;

    cout << "\nEl precio sin IVA de suelo de alta calidad es: " << high_quality << "€" << endl;
    cout << "El precio con IVA de suelo de alta calidad es: " << budget_high_quality << "€" << endl;
    cout << "\nEl precio sin IVA de suelo de media calidad es: " << middle_quality << "€" << endl;
    cout << "El prcio con IVA de suelo de media calidad es: " << budget_middle_quality << "€" << endl;
    cout << "\nEste presupuesto será válido durante " << budget_valid_days << " días" << endl;

    return 0;
}