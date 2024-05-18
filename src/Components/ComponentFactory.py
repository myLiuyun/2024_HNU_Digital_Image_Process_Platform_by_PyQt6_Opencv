# name:Gong Xiaoyv
# Time  2024-05-07   9:18

from src.Components.ComponentObjects.effects.GlassComponent import GlassComponent
from src.Components.ComponentObjects.effects.MaskComponent import MaskComponent
from src.Components.ComponentObjects.effects.OilComponent import OilComponent
from src.Components.ComponentObjects.effects.OldComponent import OldComponent
from src.Components.ComponentObjects.effects.ReliefComponent import ReliefComponent
from src.Components.ComponentObjects.effects.SketchComponent import SketchComponent
from src.Components.ComponentObjects.effects.FleetComponent import FleetComponent

from src.Components.ComponentObjects.BasicCompoonent.ImageChannelComponent import ImageChannelComponent

from src.Components.ComponentObjects.GreysComponent.HistogramEqualizationComponent import HistogramEqualizationComponent
from src.Components.ComponentObjects.GreysComponent.ConventGrayComponent import ConventGrayComponent
from src.Components.ComponentObjects.GreysComponent.BinarizationComponent import BinarizationComponent

from src.Components.ComponentObjects.FilterComponent.GaussianBlurComponent import GaussianBlurComponent
from src.Components.ComponentObjects.FilterComponent.SortedFilterComponent import SortedFilterComponent
from src.Components.ComponentObjects.FilterComponent.GradientFilterComponent import GradientFilterComponent
from src.Components.ComponentObjects.FilterComponent.BoxFilterComponent import BoxFilterComponent

from src.Components.ComponentObjects.FrequencyDomainFiltersComponent.BandFilterComponent import BandFilterComponent
from src.Components.ComponentObjects.FrequencyDomainFiltersComponent.ButterWorthFilterComponent import ButterWorthFilterComponent

from src.Components.ComponentObjects.ImageCaculateComponent.AddImageComponent import AddImageComponent

from src.Components.ComponentObjects.TransformComponent.MirrorComponent import MirrorComponent
from src.Components.ComponentObjects.TransformComponent.TranslateComponent import TransformComponent

from src.Components.ComponentObjects.ImageSegmentationComponent.LocalThresholdingComponent import LocalThresholdingComponent
from src.Components.ComponentObjects.ImageSegmentationComponent.KMeansThresholdingComponent import KMeansThresholdingComponent

from src.Components.ComponentObjects.NoiseComponent.GaussianNoiseComponent import GaussianNoiseComponent
from src.Components.ComponentObjects.NoiseComponent.SaltAndPepperNoiseComponent import SaltAndPepperNoiseComponent

from src.Components.ComponentObjects.ImageRecoveryConponent.MeanFilterComponent import MeanFilterComponent
from src.Components.ComponentObjects.ImageRecoveryConponent.TrimmedSortedFilter import TrimmedSortedFilter

from src.Components.ComponentObjects.MorphologyComponent.DilateComponent import DilateComponent
from src.Components.ComponentObjects.MorphologyComponent.ErodeComponent import ErodeComponent
from src.Components.ComponentObjects.MorphologyComponent.OpenComponent import OpenComponent
from src.Components.ComponentObjects.MorphologyComponent.CloseComponent import CloseComponent
from src.Components.ComponentObjects.MorphologyComponent.EdgeComponent import EdgeComponent

class ComponentFactory:
    component_name_map = {
        'basic':[ImageChannelComponent.name],
        'basic filters': [GaussianBlurComponent.name, SortedFilterComponent.name, GradientFilterComponent.name, BoxFilterComponent.name],
        'grey':[HistogramEqualizationComponent.name, ConventGrayComponent.name, BinarizationComponent.name],
        'effects': [GlassComponent.name, ReliefComponent.name, OilComponent.name, MaskComponent.name,
                    SketchComponent.name, OldComponent.name, FleetComponent.name],
        'Frequency Filters': [BandFilterComponent.name, ButterWorthFilterComponent.name],
        'Caculate Filters': [AddImageComponent.name],
        'Transform': [MirrorComponent.name, TransformComponent.name],
        'Image Segmentation': [LocalThresholdingComponent.name, KMeansThresholdingComponent.name],
        'Noise': [GaussianNoiseComponent.name, SaltAndPepperNoiseComponent.name],
        'Image Recovery': [MeanFilterComponent.name, TrimmedSortedFilter.name],
        'MorphologyComponent' : [DilateComponent.name ,ErodeComponent.name, OpenComponent.name, CloseComponent.name, EdgeComponent.name],
    }
    conponent_detail_key = {
        # basic
        ImageChannelComponent.name: ImageChannelComponent.detail,
        # basic filters
        GaussianBlurComponent.name: GaussianBlurComponent.detail,
        SortedFilterComponent.name: SortedFilterComponent.detail,
        GradientFilterComponent.name: GradientFilterComponent.detail,
        BoxFilterComponent.name: BoxFilterComponent.detail,
        # Grey
        HistogramEqualizationComponent.name: HistogramEqualizationComponent.detail,
        ConventGrayComponent.name: ConventGrayComponent.detail,
        BinarizationComponent.name: BinarizationComponent.detail,

        # noise
        GaussianNoiseComponent.name: GaussianNoiseComponent.detail,
        SaltAndPepperNoiseComponent.name: SaltAndPepperNoiseComponent.detail,

        # recovery
        MeanFilterComponent.name: MeanFilterComponent.detail,
        TrimmedSortedFilter.name: TrimmedSortedFilter.detail,

        # MorphologyComponent
        DilateComponent.name: DilateComponent.detail,
        ErodeComponent.name: ErodeComponent.detail,
        OpenComponent.name: OpenComponent.detail,
        CloseComponent.name: CloseComponent.detail,
        EdgeComponent.name: EdgeComponent.detail,
    }
    def __init__(self):
        pass
    def createComponent(self, componentName):
        if componentName == GaussianBlurComponent.name:
            return GaussianBlurComponent()
        elif componentName == GlassComponent.name:
            return GlassComponent()
        elif componentName == ReliefComponent.name:
            return ReliefComponent()
        elif componentName == OilComponent.name:
            return OilComponent()
        elif componentName == MaskComponent.name:
            return MaskComponent()
        elif componentName == SketchComponent.name:
            return SketchComponent()
        elif componentName == OldComponent.name:
            return OldComponent()
        elif componentName == FleetComponent.name:
            return FleetComponent()
        elif componentName == ImageChannelComponent.name:
            return ImageChannelComponent()
        elif componentName == HistogramEqualizationComponent.name:
            return HistogramEqualizationComponent()
        elif componentName == ConventGrayComponent.name:
            return ConventGrayComponent()
        elif componentName == BinarizationComponent.name:
            return BinarizationComponent()
        elif componentName == SortedFilterComponent.name:
            return SortedFilterComponent()
        elif componentName == GradientFilterComponent.name:
            return GradientFilterComponent()
        elif componentName == BoxFilterComponent.name:
            return BoxFilterComponent()
        elif componentName == BandFilterComponent.name:
            return BandFilterComponent()
        elif componentName == ButterWorthFilterComponent.name:
            return ButterWorthFilterComponent()
        elif componentName == AddImageComponent.name:
            return AddImageComponent()
        elif componentName == MirrorComponent.name:
            return MirrorComponent()
        elif componentName == TransformComponent.name:
            return TransformComponent()
        elif componentName == LocalThresholdingComponent.name:
            return LocalThresholdingComponent()
        elif componentName == KMeansThresholdingComponent.name:
            return KMeansThresholdingComponent()
        elif componentName == GaussianNoiseComponent.name:
            return GaussianNoiseComponent()
        elif componentName == SaltAndPepperNoiseComponent.name:
            return SaltAndPepperNoiseComponent()
        elif componentName == MeanFilterComponent.name:
            return MeanFilterComponent()
        elif componentName == TrimmedSortedFilter.name:
            return TrimmedSortedFilter()
        elif componentName == DilateComponent.name:
            return DilateComponent()
        elif componentName == ErodeComponent.name:
            return ErodeComponent()
        elif componentName == OpenComponent.name:
            return OpenComponent()
        elif componentName == CloseComponent.name:
            return CloseComponent()
        elif componentName == EdgeComponent.name:
            return EdgeComponent()
        else:
            raise Exception(f"ComponentFactory:: Component {componentName} not found")