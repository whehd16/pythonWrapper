package preprocessing;

import java.io.*;

import java.util.List;
import weka.core.Instances;
import weka.classifiers.functions.GaussianProcesses;
import weka.classifiers.evaluation.NumericPrediction;
import weka.classifiers.timeseries.WekaForecaster;

public class forecast {

    public static void main(String[] args) {
        try {

            Instances dataset = new Instances(new BufferedReader(new FileReader("dataset/appl.arff")));
            dataset.sort(0);

            WekaForecaster forecaster = new WekaForecaster();
            forecaster.setFieldsToForecast("Close");

            forecaster.setBaseForecaster(new GaussianProcesses());

            forecaster.getTSLagMaker().setTimeStampField("Date");
            forecaster.getTSLagMaker().setMinLag(12);
            forecaster.getTSLagMaker().setMaxLag(24);

            forecaster.buildForecaster(dataset);

            forecaster.primeForecaster(dataset);

            List<NumericPrediction> predsAtStep = forecast.get(i);
            NumericPrediction predForTarget = predsAtStep.get(0);
            System.out.println("" + predForTarget.predicted() + " ");

        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
