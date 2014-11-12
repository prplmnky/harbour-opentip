import QtQuick 2.0
import Sailfish.Silica 1.0
import harbour.opentip.QmlLogger 2.0
import "pages"
import "cover"

ApplicationWindow
{
    initialPage: Component {
        MainApp {
            id: mainApp

            onFinalAmountChanged: coverPage.total = amount
            onTipAmountChanged: coverPage.tip = amount
        }
    }
    cover: CoverPage {id: coverPage}

    Component.onCompleted: {
        Console.LOG_PRIORITY = Console.INFO
    }
}


