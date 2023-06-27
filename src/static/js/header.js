function addWidthAndHeightToBanner() {
    const images = document.querySelectorAll('.carousel-item img');
    const widthScreen = window.innerWidth;
    const bannerSizes = {
        small: {
            screenWidth: 576,
            sizes: {
                width: 576, height: 324
            }
        },
        medium: {
            screenWidth: 768,
            sizes: {
                width: 768, height: 432
            }
        },
        large: {
            screenWidth: 1920,
            sizes: {
                width: 1920, height: 1080
            }
        }
    }
    let currentSize;

    if (widthScreen <= bannerSizes.small.screenWidth) {
        currentSize = bannerSizes.small.sizes;
    } else if (widthScreen <= bannerSizes.medium.screenWidth) {
        currentSize = bannerSizes.medium.sizes;
    } else {
        currentSize = bannerSizes.large.sizes;
    }

    images.forEach(img => {
        img.width = currentSize.width;
        img.height = currentSize.height;
    });
}

//addWidthAndHeightToBanner();