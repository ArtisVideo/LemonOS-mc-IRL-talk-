using System.ComponentModel;
using Xamarin.Forms;
using Xamrin.ViewModels;

namespace Xamrin.Views
{
    public partial class ItemDetailPage : ContentPage
    {
        public ItemDetailPage()
        {
            InitializeComponent();
            BindingContext = new ItemDetailViewModel();
        }
    }
}